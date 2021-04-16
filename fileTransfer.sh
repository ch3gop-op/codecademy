#!/bin/bash
#ch3gop.op codecademy bash scripting project 

echo "welcome to the file transfer script."

firstline=$(head -n 1 source/changelog.md)

read -a splitfirstline <<< $firstline 

version=${splitfirstline[1]}
echo "You are building verion " $version
echo "Do you want to continue? (enter "1" for yes, "0" for no)"
read versioncontinue 

if [ $versioncontinue -eq 1 ]
then
  echo "OK"
  for file in source/*
  do
    echo $file
    if [ "$file" == "source/secretinfo.md" ]
    then
      echo "Not copying" $file
    else
      echo "Copying" $file
      cp $file build/.
    fi
  done
  cd build/
  echo "Build version $version contains:"
  ls -ltr
  cd ..
else
  echo "Please come back when you are ready"
fi

