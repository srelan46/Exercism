class SqueakyClean {
    static String clean(String identifier) {
       char arr[] = identifier.toCharArray();
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<arr.length;i++){
            if(Character.isDigit(arr[i])){
                   switch (arr[i]) {
                    case '4': sb.append('a'); break;
                    case '3': sb.append('e'); break;
                    case '0': sb.append('o'); break;
                    case '1': sb.append('l'); break;
                    case '7': sb.append('t'); break;
                   }
            }
            else if(Character.isWhitespace(arr[i]))
                sb.append('_');
            else if(arr[i]=='-' && i+1<arr.length){
                 char temp = Character.toUpperCase(arr[++i]);
                sb.append(temp);
            }
            else if(Character.isLetter(arr[i]))
                sb.append(arr[i]);
        }
        return sb.toString();
    }
}
