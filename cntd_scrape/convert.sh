
for file in `ls cntd/`
do
	echo $file
	iconv -f UTF8 -t GB18030 cntd/$file >cntdf/$file
done
