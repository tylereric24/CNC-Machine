grammar turtle;

start : expr | <EOF> ;

expr     : 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr    
         | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr
         | 'G03' x_cord=NUMBER y_cord=NUMBER  #drawExpr
         | 'G28' x_cord=NUMBER y_cord=NUMBER #HomeExpr
         ;
NUMBER :('-')? ('0' .. '9') + ('.' ('0' .. '9') +)? ;
WS : [ \r\n\t]+ -> skip;

