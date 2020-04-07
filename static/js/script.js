$(document).ready(()=>{
    var socket = io.connect('http://localhost:5000');
    
    socket.on('message', (msg)=> {
        $("#message-ul").append("<li>" + msg + "</li>")
    });

    $("#send-button").click((target)=>{
        console.log("clicked");
        socket.emit(
            'message', 
            $('#message-input').val()
        );
        $('#message-input').val('') //clear input text
    });
    $("#message-input").keypress((e)=>{
        if (e.which == 13){//enter
            $("#send-button").click();
        }
    });
 });