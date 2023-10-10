mkfifo $1
python3 ./check.py $1 &
echo "testdata" > $1
python3 ./write.py $1 &
python3 ./read.py $1 &
