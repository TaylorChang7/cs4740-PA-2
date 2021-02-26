#!/bin/bash

CORRECT=0

tmpoutput=`echo -e 6 '\n' 5 | python $1`
f1=`echo $tmpoutput | grep -q '1'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi

tmpoutput=`echo -e 10 '\n' 2 | python $1`
f1=`echo $tmpoutput | grep -q '2'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi

exit $CORRECT
