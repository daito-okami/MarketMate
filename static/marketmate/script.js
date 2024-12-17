function scrollOffers(direction) {
    const container = document.getElementById('offersContainer');
    const scrollAmount = 300;

    if (direction === 'left') {
      container.scrollBy({
        left: -scrollAmount,
        behavior: 'smooth'
      });
    } else {
      container.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
      });
    }
  }

  // Handle search functionality
  function handleSearch() {
    const searchValue = document.getElementById('searchInput').value;
    console.log('Search value:', searchValue);
    // TODO: Implement backend search functionality
  }

  document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      handleSearch();
    }
  });

  // Recipe scroll functionality
let scrollAmount = 300; // Amount to scroll each time
let scrollTimeout; // For debouncing

function scrollRecipes(direction) {
  const container = document.querySelector('.recipes-slider');
  const currentScroll = container.scrollLeft;
  const maxScroll = container.scrollWidth - container.clientWidth;

  // Calculate new scroll position
  const newScroll = direction === 'left'
    ? Math.max(0, currentScroll - scrollAmount)
    : Math.min(maxScroll, currentScroll + scrollAmount);

  // Perform the scroll
  container.scrollTo({
    left: newScroll,
    behavior: 'smooth'
  });

  // Update button visibility
  updateScrollButtons(container);
}

function updateScrollButtons(container) {
  const leftButton = document.querySelector('.scroll-left');
  const rightButton = document.querySelector('.scroll-right');

  // Show/hide buttons based on scroll position
  if (leftButton && rightButton) {
    leftButton.style.opacity = container.scrollLeft <= 0 ? '0.5' : '1';
    rightButton.style.opacity =
      container.scrollLeft >= container.scrollWidth - container.clientWidth
        ? '0.5'
        : '1';
  }
}

// Add scroll event listener for updating button states
document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.recipes-slider');
  if (container) {
    container.addEventListener('scroll', () => {
      // Debounce the update
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => updateScrollButtons(container), 150);
    });

    // Initial button state
    updateScrollButtons(container);
  }
});

// Optional: Add touch/swipe support
let touchStart = null;
let touchX = null;

document.querySelector('.recipes-slider')?.addEventListener('touchstart', (e) => {
  touchStart = e.touches[0].clientX;
}, false);

document.querySelector('.recipes-slider')?.addEventListener('touchmove', (e) => {
  if (!touchStart) return;

  touchX = e.touches[0].clientX;
  const diff = touchStart - touchX;

  // Prevent default scrolling
  if (Math.abs(diff) > 5) {
    e.preventDefault();
  }
}, false);

document.querySelector('.recipes-slider')?.addEventListener('touchend', () => {
  if (!touchStart || !touchX) return;

  const diff = touchStart - touchX;
  const threshold = 50; // minimum distance for swipe

  if (Math.abs(diff) > threshold) {
    scrollRecipes(diff > 0 ? 'right' : 'left');
  }

  // Reset values
  touchStart = null;
  touchX = null;
}, false);