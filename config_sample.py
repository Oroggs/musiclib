TEMP_PATH = '/dev/shm'

SQL_ADDR = ''
SQL_USER = ''
SQL_PASSWORD = ''
SQL_DATABASE = ''

SQL_URI = 'mysql+mysqlconnector://%s:%s@%s/%s'%(SQL_USER, SQL_PASSWORD, SQL_ADDR, SQL_DATABASE)

STORAGE_PATH = ''
STORAGE_SALT = b''

BACKUP_PATH = ''

TRUSTED_EXTENSIONS = ['zip', 'rar', '7z', 'log', 'txt', 'jpg']

DEBUG = True
