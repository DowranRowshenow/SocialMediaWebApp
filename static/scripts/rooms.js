/* VARIABLES */
//const roomToken = JSON.parse(document.getElementById('json-roomToken').textContent);
//const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/rooms/' + roomToken + '/');

/* MAIN */
scrollToBottom();

/* WEBSOCKETS */
/*
chatSocket.onmessage = function(e) 
{
    const data = JSON.parse(e.data);
    if (data.content) {
        let html = '';

        if (userName == data.userName)
        {
            html += '<div class="message_box_rigth right margin_right_20">';
            html +=     '<div class="message_right">';
            html +=         '<a class="message_text">' + data.content + '</a>';
            html +=     '</div>';
            html +=     '<div><a>' + data.sent_date_time + '</a></div>';
            html += '</div>';
            html += '<div id="chat_spacer" class="message_user spacer">&nbsp;</div>';
        } 
        else 
        {
            html += '<div class="message_user message_box">';
            html +=     '<div class="user_field top">';
            html +=         '<img class="user_field_img radius_20" src="' + data.image + '" alt="profile.png"></img>';
            html +=     '</div>'; 
            html +=     '<div class="message_field">'; 
            html +=         '<a class="message_field_text">' + data.userName + '</a>'; 
            html +=         '<div class="message">'; 
            html +=             '<a class="message_text">' + data.content + '</a>'; 
            html +=         '</div>'; 
            html +=         '<div><a>' + data.sent_date_time + '</a></div>';
            html +=     '</div>'; 
            html += '</div>';
            html += '<div id="chat_spacer" class="message_user spacer">&nbsp;</div>';
        }
        chat_spacer.remove();
        chat_messages.innerHTML += html;
        scrollToBottom();
    } 
    else 
    {
        alert("You can not send empty messages!");
    }
}
function send_message()
{
    var content = chat_message_input.value;
    content = content.replace("<","&lt;");
    content = content.replace(">","&gt;");
    chatSocket.send(JSON.stringify({
        'content': content,
    }));
    chat_message_input.value = '';
}
*/
/*
function send_message() {
    var content = document.getElementById("chat_message_input").value;
    content = content.replace("<", "&lt;");
    content = content.replace(">", "&gt;");
    fetch(`/send_message/${roomToken}/`, {
        method: 'POST',
        body: JSON.stringify({
            'content': content,
        }),
    });
    document.getElementById("chat_message_input").value = '';
    return false;
}*/
/* FUNCTIONS */
function send_message() {
    var content = document.getElementById("chat_message_input").value;
    content = content.replace("<", "&lt;");
    content = content.replace(">", "&gt;");
    /*
    fetch(`/send_message/${roomToken}/`, {
        method: 'POST',
        body: JSON.stringify({
            'content': content,
        }),
    });
    */
    document.getElementById("chat_message_input").value = '';
    return false;
}
var input = document.getElementById("chat_message_input");
input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        //send_message();
        document.getElementById('send_form').submit();
    }
});
function scrollToBottom() {
    try { chat_messages.scrollTo({ top: chat_messages.scrollHeight, behavior: 'smooth' }); }
    catch { }
}