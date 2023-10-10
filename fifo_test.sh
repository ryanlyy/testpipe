typeset -i idx=0

while [[ $idx -le 2000 ]]; do
        idx=$idx+1
        FF_NAME=./fifo200-$idx
        echo "$FF_NAME"
	./def $FF_NAME
#        mkfifo ./fifo200-$idx
#        python3 ./check.py ./fifo200-$idx &
#        echo "testdata" > ./fifo200-$idx 
done
