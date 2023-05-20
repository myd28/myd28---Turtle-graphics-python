grammar turtle; 

start : expr | <EOP> ; 

expr : 'G01' x_cord=NUMBER y_cord=NUMBER #drawlineExpr       
     | 'G02' x_cord=NUMBER y_cord=NUMBER i_cord=NUMBER #drawCircleG02 
     | 'G03' x_cord= NUMBER y_cord= NUMBER i_cord= NUMBER #drawCircleG03 
     | 'G91' x_cord= NUMBER y_cord= NUMBER #positioningG91 
     | 'print' x_cord=NUMBER y_cord=NUMBER #printlineExpr 
     ; 


     NUMBER :('-'+)? ('0' .. '9') + ('.' ('0' .. '9') +)? ; 
     WS : [ \r\n\t]+ ->skip;  	   
