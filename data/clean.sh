s(){ source $BASH_SOURCE; }
v(){ vi $BASH_SOURCE; }
c(){ shellcheck $BASH_SOURCE; }
alias t='clean-readbyline FIN.cMx_1x1.txt'

clean-readbyline(){
    while read line; do
        re="^[0-9]+"
        re2="\. \s{1}"
        #if [[ $line =~ $re ]] && [[ $line =~ $re2 ]]  ; then
        if [[ $line =~ $re2 ]]  ; then
             echo $line
        fi
    done < $1
}

clean-read(){
    while read line; do
        IFS=' '; 
        linearray=()
        for word in $line; do
               linearray+=($word); 
        done
        IFS=$' \t\n'
        re='^[0-9]+$'
        if [[ ${linearray[0]} =~ $re ]]; then
            containsElement "." "${linearray[@]}"
            if [[ $? = 0 ]]; then # $? is the return value, 0=noerror=true
             echo $line
            fi
        fi
    done < $1
}


containsElement () {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}
