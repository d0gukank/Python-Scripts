function object2text(x) {
 //[object Object] > text
 var buffer = Java.array('byte', x);
 var result = "";
 for(var i = 0; i < buffer.length; ++i){
     result+= (String.fromCharCode(buffer[i]));
 }
   return result;

}




function text2base64(x) {
 //[object Object] > base64
var androidBase64 = Java.use('android.util.Base64')
var bytesInJava = androidBase64.encodeToString(x,2)
return bytesInJava;
}







function bin2ascii(array) {
    var result = [];

    for (var i = 0; i < array.length; ++i) {
        result.push(String.fromCharCode( // hex2ascii part
            parseInt(
                ('0' + (array[i] & 0xFF).toString(16)).slice(-2), // binary2hex part
                16
            )
        ));
    }
    return result.join('');
}



function bin2hex(array, length) {
    var result = "";

    length = length || array.length;

    for (var i = 0; i < length; ++i) {
        result += ('0' + (array[i] & 0xFF).toString(16)).slice(-2);
    }
    return result;
}

