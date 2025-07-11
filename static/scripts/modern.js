// Modern JavaScript for enhanced UX

// Modern UI Class
class ModernUI {
    constructor() {
        this.init();
    }

    init() {
        this.setupLoadingIndicator();
        this.setupScrollProgress();
        this.setupMobileNavigation();
        this.setupAnimations();
        this.setupToastNotifications();
        this.setupKeyboardShortcuts();
    }

    // Loading Indicator
    setupLoadingIndicator() {
        const loadingIndicator = document.getElementById('loading-indicator');
        if (loadingIndicator) {
            // Hide loading indicator when page is fully loaded
            window.addEventListener('load', () => {
                setTimeout(() => {
                    loadingIndicator.classList.add('hidden');
                }, 500);
            });
        }
    }

    // Scroll Progress Bar
    setupScrollProgress() {
        const progressBar = document.getElementById('scroll-progress');
        if (!progressBar) return;

        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset;
            const docHeight = document.body.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            progressBar.style.width = scrollPercent + '%';
        });
    }

    // Mobile Navigation
    setupMobileNavigation() {
        const mobileToggle = document.getElementById('mobile-nav-toggle');
        const nav = document.getElementById('nav');
        const side = document.getElementById('side');

        if (mobileToggle && nav) {
            mobileToggle.addEventListener('click', () => {
                nav.classList.toggle('mobile-open');
                mobileToggle.classList.toggle('active');
            });
        }

        // Close mobile nav when clicking outside
        document.addEventListener('click', (e) => {
            if (nav && nav.classList.contains('mobile-open')) {
                if (!nav.contains(e.target) && !mobileToggle.contains(e.target)) {
                    nav.classList.remove('mobile-open');
                    mobileToggle.classList.remove('active');
                }
            }
        });
    }

    // Smooth Animations
    setupAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.querySelectorAll('.post, .message_box, .profile_box').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'all 0.6s ease-out';
            observer.observe(el);
        });
    }

    // Toast Notifications
    setupToastNotifications() {
        this.toastContainer = document.createElement('div');
        this.toastContainer.className = 'toast-container';
        this.toastContainer.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
        `;
        document.body.appendChild(this.toastContainer);
    }

    showToast(message, type = 'info', duration = 3000) {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.style.cssText = `
            background: var(--bg-elevated);
            color: var(--text-primary);
            padding: 1rem 1.5rem;
            border-radius: 12px;
            border: 1px solid var(--border-light);
            box-shadow: var(--shadow-xl);
            transform: translateX(100%);
            transition: transform 0.3s ease;
            max-width: 300px;
            word-wrap: break-word;
        `;
        toast.textContent = message;

        this.toastContainer.appendChild(toast);

        // Animate in
        setTimeout(() => {
            toast.style.transform = 'translateX(0)';
        }, 100);

        // Auto remove
        setTimeout(() => {
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 300);
        }, duration);
    }

    // Keyboard Shortcuts
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl/Cmd + K for search
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                const searchInput = document.querySelector('.search_bar_input');
                if (searchInput) {
                    searchInput.focus();
                }
            }

            // Escape to close modals
            if (e.key === 'Escape') {
                this.closeAllModals();
            }

            // Ctrl/Cmd + Enter to submit forms
            if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                const activeForm = document.querySelector('form:focus-within');
                if (activeForm) {
                    activeForm.submit();
                }
            }
        });
    }

    closeAllModals() {
        document.querySelectorAll('.section.visible').forEach(section => {
            section.classList.remove('visible');
        });
    }
}

// Initialize Modern UI when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.modernUI = new ModernUI();
});

// Enhanced existing functions
function open_section(section, ...args) {
    if (section) {
        section.classList.add('visible');
        section.style.animation = 'fadeIn 0.3s ease-out';

        // Handle specific sections
        if (section.id === 'image_section' && args[0]) {
            document.getElementById('image_section_image').src = args[0];
        }

        if (section.id === 'edit_post_section') {
            if (args[1]) {
                document.getElementById('edit_post_form_content_input').value = args[1];
            }
            if (args[0]) {
                document.getElementById('edit_post_form_image_input').value = '';
            }
        }
    }
}

function close_section(section) {
    if (section) {
        section.classList.remove('visible');
        section.style.animation = 'fadeOut 0.3s ease-out';
    }
}

// Enhanced scroll functions
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function scrollToBottom() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    });
}

// Enhanced dropdown function
function on_dropdown_click(dropdown) {
    if (dropdown) {
        dropdown.classList.toggle('show');

        // Close other dropdowns
        document.querySelectorAll('.dropdown-content.show').forEach(d => {
            if (d !== dropdown) {
                d.classList.remove('show');
            }
        });
    }
}

// Close dropdowns when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.matches('.dropbtn')) {
        document.querySelectorAll('.dropdown-content.show').forEach(dropdown => {
            dropdown.classList.remove('show');
        });
    }
});

// Enhanced friend request function
function friend_request(username = null) {
    const input = document.getElementById('friend_request_form_input');
    const error = document.getElementById('friend_request_form_error');
    const loader = document.getElementById('friend_section_loader');

    if (!username) {
        username = input.value.trim();
    }

    if (!username) {
        if (window.modernUI) {
            window.modernUI.showToast('Username is required', 'error');
        }
        return;
    }

    // Show loading
    if (loader) loader.classList.add('show');

    // Simulate API call
    setTimeout(() => {
        if (loader) loader.classList.remove('show');
        if (window.modernUI) {
            window.modernUI.showToast('Friend request sent to ' + username, 'success');
        }
        close_section(document.getElementById('friend_section'));
        input.value = '';
    }, 1000);
}

// Enhanced send message function
function send_message() {
    const input = document.getElementById('chat_message_input');
    const message = input.value.trim();

    if (!message) {
        if (window.modernUI) {
            window.modernUI.showToast('Please enter a message', 'error');
        }
        return;
    }

    // Add message to chat
    const chatMessages = document.getElementById('chat_messages');
    const messageElement = document.createElement('div');
    messageElement.className = 'message_box_rigth right margin_right_20';
    messageElement.innerHTML = `
        <div class="message_right">
            <a class="message_text font_light">${message}</a>
        </div>
        <div><a>Just now</a></div>
    `;

    chatMessages.appendChild(messageElement);
    input.value = '';

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;

    if (window.modernUI) {
        window.modernUI.showToast('Message sent', 'success');
    }
}

// Enhanced send comment function
function send_comment() {
    const input = document.getElementById('chat_message_input');
    const comment = input.value.trim();

    if (!comment) {
        if (window.modernUI) {
            window.modernUI.showToast('Please enter a comment', 'error');
        }
        return;
    }

    // Add comment to post
    const chatMessages = document.getElementById('chat_messages');
    const commentElement = document.createElement('div');
    commentElement.className = 'right';
    commentElement.innerHTML = `
        <div class="message_box_rigth right margin_right_20">
            <div class="message_right">
                <a class="message_text font_light">${comment}</a>
            </div>
            <div>Just now</div>
        </div>
    `;

    chatMessages.appendChild(commentElement);
    input.value = '';

    // Update comment count
    const commentCount = document.getElementById('post_comment_count');
    if (commentCount) {
        const currentCount = parseInt(commentCount.textContent) || 0;
        commentCount.textContent = currentCount + 1;
    }

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;

    if (window.modernUI) {
        window.modernUI.showToast('Comment posted', 'success');
    }
}

// Enhanced like/dislike functions
function like_post() {
    const likesElement = document.getElementById('likes');
    if (likesElement) {
        const currentLikes = parseInt(likesElement.textContent) || 0;
        likesElement.textContent = currentLikes + 1;
        if (window.modernUI) {
            window.modernUI.showToast('Post liked!', 'success');
        }
    }
}

function dislike_post() {
    const dislikesElement = document.getElementById('dislikes');
    if (dislikesElement) {
        const currentDislikes = parseInt(dislikesElement.textContent) || 0;
        dislikesElement.textContent = currentDislikes + 1;
        if (window.modernUI) {
            window.modernUI.showToast('Post disliked', 'info');
        }
    }
}

// Enhanced page navigation
function page(pageName) {
    const currentUrl = new URL(window.location);
    currentUrl.searchParams.set('pg', pageName);
    window.location.href = currentUrl.toString();
}

// Enhanced grouper function
function grouper(group, icon) {
    if (group && icon) {
        group.style.display = group.style.display === 'none' ? 'block' : 'none';
        icon.style.transform = group.style.display === 'none' ? 'rotate(0deg)' : 'rotate(180deg)';
    }
}

// Enhanced clear URL function
function clearUrl(page) {
    const currentUrl = new URL(window.location);
    if (page) {
        currentUrl.searchParams.set('pg', page);
    }
    currentUrl.searchParams.delete('pd');
    window.location.href = currentUrl.toString();
}

// Enhanced animations
function animaitons() {
    const animationsCheckbox = document.getElementById('animations');
    if (animationsCheckbox) {
        const enabled = animationsCheckbox.checked;
        document.body.style.setProperty('--transition-fast', enabled ? '150ms ease-in-out' : '0ms');
        document.body.style.setProperty('--transition-normal', enabled ? '250ms ease-in-out' : '0ms');
        document.body.style.setProperty('--transition-slow', enabled ? '350ms ease-in-out' : '0ms');
    }
}

// Enhanced cursor function
function cursor() {
    const cursorCheckbox = document.getElementById('cursor');
    if (cursorCheckbox) {
        const enabled = cursorCheckbox.checked;
        document.body.style.cursor = enabled ? 'default' : 'none';
    }
}

// Enhanced text area function
function TextArea(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
}
