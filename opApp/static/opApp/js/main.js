const topNav = document.querySelector('.topNav');
const clickNav = document.querySelector('#menuButton');
// scroll for nav
window.onscroll = function(){
    let top = window.scrollY;
    if (top > 1){
        topNav.classList.add('active');
    }else{
        topNav.classList.remove('active');
    }
}
// click for nav
clickNav.addEventListener('click', (e)=>{
    topNav.classList.add('active');
})

const galleryItems = document.querySelectorAll('.galleryItem');
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalSkills = document.getElementById('modal-skills');
const modalImg = document.querySelector('.modal-body img');
const modalDescription = document.getElementById('modal-description');
const modalVisitSite = document.getElementById('modal-visit-site');
const closeButton = document.querySelector('.close');

galleryItems.forEach((item, index) => {
    const viewProjectButton = item.querySelector('.btnGallery');
    viewProjectButton.addEventListener('click', (e) => {
        e.preventDefault();
        fetch('/get-works/')
            .then(response => response.json())
            .then(data => {
                const works = data.works;
                modalTitle.textContent = works[index].title;
                modalSkills.textContent = works[index].skills;
                modalImg.src = '/media/'+works[index].modal_image;
                modalDescription.textContent = works[index].modal_description;
                modalVisitSite.href = works[index].link;
                modal.style.display = 'block';
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    });
});

if (closeButton) {
    closeButton.addEventListener('click', () => {
        modal.style.display = 'none';
    });
}

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// CHATBOT

document.addEventListener("DOMContentLoaded", function() {
    const messagesList = document.querySelector('.messages-list');
    const messageForm = document.querySelector('.message-form');
    const messageInput = document.querySelector('.message-input');

    if (messageForm) {
        messageForm.addEventListener('submit', (event) => {
            event.preventDefault();

            const message = messageInput.value.trim();
            if (message.length === 0) {
                return;
            }

            const messageItem = document.createElement('li');
            messageItem.classList.add('message', 'sent');
            messageItem.innerHTML = `
                <div class="message-text user">
                    <div class="message-sender">
                        <b>You</b>
                    </div>
                    <div class="message-content">
                        ${message}
                    </div>
                </div>`;
            messagesList.appendChild(messageItem);

            messageInput.value = '';

            fetch('/opApp/chatbot/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({
                    'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'message': message
                })
            })
            .then(response => response.json())
            .then(data => {
                const response = data.response;
                const messageItem = document.createElement('li');
                messageItem.classList.add('message', 'received');
                messageItem.innerHTML = `
                <div class="message-text bot">
                    <div class="message-sender">
                        <b>nicoAI</b>
                    </div>
                    <div class="message-content">
                        ${response}
                    </div>
                </div>
                    `;
                messagesList.appendChild(messageItem);
            });
        });
    }
    const activateChatbotBtn = document.querySelector('.activate-chatbot');
    const closeIcon = document.querySelector('.close-icon');
    const chatContainer = document.querySelector('.chat-container');

    if (activateChatbotBtn) {
        activateChatbotBtn.addEventListener('click', function() {
            if (chatContainer.style.display === 'block') {
                chatContainer.style.display = 'none';
            } else {
                chatContainer.style.display = 'block';
            }
        });

        closeIcon.addEventListener('click', function() {
            chatContainer.style.display = 'none';
        });
    }
});