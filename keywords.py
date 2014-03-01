RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'

token_exprs = [
	(r'[ \t]+',                None),
	(r'#[^\n]*',               None),
	(r'\n',                    RESERVED),
	(r'BEGIN',                 RESERVED),
	(r'END',                   RESERVED),
	(r'SKIP',                  RESERVED),
	(r'VAR',                   RESERVED),
	(r'SET',                   RESERVED),
	(r'PRINT',                 RESERVED),
	(r'\+',                    RESERVED),
	(r'-',                     RESERVED),
	(r'\*',                    RESERVED),
	(r'/',                     RESERVED),
	(r'<=',                    RESERVED),
	(r'<',                     RESERVED),
	(r'>=',                    RESERVED),
	(r'>',                     RESERVED),
	(r'!=',                    RESERVED),
	(r'=',                     RESERVED),
]
