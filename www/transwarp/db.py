

import threading

_dbctx = _DbCtx()
def update(sql,*args):
	global _dbctx
	cursor = None
	try:
		if _dbctx.is_init() == False:
			_dbctx.init()
		cursor = _dbctx.cursor()
		cursor.execute(sql,args)
		_dbctx.connection.commit()
		return cursor.rowcount
	finally:
		if cursor:
			cursor.cleanup()





class _DbCtx(threading.local):
	def __init__(self):
		self.connection = None
		super(_DbCtx, self).__init__()

	def is_init():
		return not self.connection is None

	def init(self):
		self.connection = _LasyConnection()

	def cleanup(self):
		if self.connection:
			self.connection.cleanup()

	def cursor(self):
		if self.connection:
			return self.connection.cursor()



class _LasyConnection(object):
	def __init__(self):
		self.connect = None
		super(_LasyConnection, self).__init__()

	def cursor(self):
		if self.connect is None:
			self.connect = engine.connect()
		return self.connect.cursor()

	def commit(self):
		if self.connect is None:
			self.connect = engine.connect()
		return self.connect.commit()

	def rollback(self):
		if self.connect:
			self.connect.rollback()

	def cleanup(self):
		if self.connect:
			self.connect.close()
			self.connect = None;
		


class _Engine(object):
	def __init__(self, connect):
		super(_Engine, self).__init__()
		self.connect = connect
	def connect(self):
		return self.connect()


engine = None
def creat_connect(user='root',password='password',database='test',host='127.o.0.1',port=3306):
	import mysql.connector
	parmer = dict(user=user, password=password, database=database, host=host, port=port)
	global engine
	engine = _Engine(lambda: mysql.connector.connect(**parmer))



if __name__ == '__main__':
	creat_connect('','','test')

