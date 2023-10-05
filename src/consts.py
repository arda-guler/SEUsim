from binary import *

cpu_add =       Binary(65535)
cpu_sub =       Binary(65534)
cpu_mod_reg1 =  Binary(65533)
cpu_mod_reg2 =  Binary(65532)
cpu_jmp =       Binary(65531)
cpu_jg =        Binary(65530)
cpu_jl =        Binary(65529)
cpu_je =        Binary(65528)
cpu_write =     Binary(65527)
cpu_recall =    Binary(65526)
cpu_memwrite =  Binary(65525)
cpu_memread =   Binary(65524)
cpu_halt =      Binary(65523)
NULL =          Binary(0)

upset_values = [Binary(1),
                Binary(2),
                Binary(4),
                Binary(8),
                Binary(16),
                Binary(32),
                Binary(64),
                Binary(128),
                Binary(256),
                Binary(512),
                Binary(1024),
                Binary(2048),
                Binary(4096),
                Binary(8192),
                Binary(16384),
                Binary(32768)]
