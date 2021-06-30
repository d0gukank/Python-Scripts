 Module.enumerateExports("xx-utils.so", {                
      onMatch: function(e) {                            
    if(e.type == 'function') {
		console.log("name of function = " + e.name);

    if(e.name == "Java_xxx_NativeEncryptionUtils_encryptData") {
		console.log("Function Decrypt recognized by name");
		Interceptor.attach(e.address, {       
		onEnter: function(args) {         
			console.log("Interceptor attached onEnter...");
			},                                
		onLeave: function(retval){        
			console.log("Interceptor onLeave");
			}                                 
		});                                                                   
              }                   
          }   
      },                                                
      onComplete: function() {}                         
  });  
