#! /bin/bash

MSG_SANITIZED=$(echo $* | tr -d [:space:])

SIZE=$(echo -n $MSG_SANITIZED | wc -c)

if [ $SIZE -eq 0 ]
then
	exit 0
fi

if [ $SIZE -lt 2 ]
then
	echo $MSG_SANITIZED
	exit 0
fi

MIDDLE=$(($SIZE / 2))

PART1=$(echo -n $MSG_SANITIZED | cut -c -$MIDDLE)
PART2=$(echo -n $MSG_SANITIZED | cut -c $(($MIDDLE + 1))-)

SET1=$(echo -n $PART1 | sed -e 's/\(..\)/\1 /g')
SET2=$(echo -n $PART2 | sed -e 's/\(..\)/\1 /g')

for E1 in $SET1
do
	for E2 in $SET2
	do
		echo -n "$E1$E2 "
	done
done
echo

