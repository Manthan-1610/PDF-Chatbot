css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngegg.com%2Fen%2Fsearch%3Fq%3Dchatbot&psig=AOvVaw2O_eGmUmjVZglHko64inl-&ust=1690807247945000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqGAoTCOCrmf25toADFQAAAAAdAAAAABCHAQ" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.iconfinder.com%2Ficons%2F309035%2Fuser_account_human_person_icon&psig=AOvVaw1prQtBLsuKzaG_BX_5xAiu&ust=1690807556609000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOjoo5C7toADFQAAAAAdAAAAABAJ">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''