const uploadButton = document.querySelector('.upload-button');
const uploadInput = document.getElementById('uploadInput');
const uploadedImage = document.getElementById('uploadedImage');
const plantName = document.getElementById('plantName');
const medicineText = document.getElementById('medicineText');

uploadButton.addEventListener('click', () => {
  uploadInput.click(); // Trigger file input click when the button is clicked
});

uploadInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  
  reader.onload = function() {
    uploadedImage.src = reader.result;
  }
  
  reader.readAsDataURL(file);

  // Simulating plant recognition and medicine prediction
  predictPlantMedicine(file);
});

function predictPlantMedicine(file) {
  // Placeholder function to simulate plant recognition and medicine prediction
  // You would replace this with actual logic to predict the plant and medicine
  // Here, we are just simulating with a timeout
  setTimeout(() => {
    const plantNameFromImage = "Sample Plant Name";
    const medicineInfo = "Sample Medicine Information...";
    plantName.textContent = `Plant Name: ${plantNameFromImage}`;
    animateTypewriter(medicineInfo);
  }, 2000); // Simulating a delay of 2 seconds for prediction
}

function animateTypewriter(text) {
  let charIndex = 0;
  const interval = setInterval(() => {
    if (charIndex <= text.length) {
      medicineText.textContent = text.substring(0, charIndex++);
    } else {
      clearInterval(interval);
    }
  }, 100); // Adjust typing speed as needed
}
