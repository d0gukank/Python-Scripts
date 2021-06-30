 Module.enumerateExports("xx-utils.so", {                
      onMatch: function(e) {                            
    if(e.type == 'function') {
		//console.log("name of function = " + e.name);

    if(e.name == "Java_com_xxxxx_utils_NativeEncryptionUtils_encryptData") {
		console.log("Function encrypt recognized by name");
		Interceptor.attach(e.address, {       
		onEnter: function(args) {         
			console.log("Interceptor attached onEnter...");
			var data = Memory.readByteArray(args[0], 100);
        console.log("Memory data: ");
        console.log(data);
                     console.log(JSON.stringify({
                        a1: Memory.readCString(Memory.readPointer(args[0]))
               
            
                    }, null, '\t'));

			},                                
		onLeave: function(retval){        
			console.log("Interceptor onLeave");

			console.log("ret: " + retval);
			}                                 
		});                                                                   
              }                   
          }   
      },                                                
      onComplete: function() {}                         
  });  



