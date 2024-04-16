const form = document.getElementById("form");
const loading = document.getElementById("loading");
const result = document.getElementById("result");

const handleSubmit = (e) => {
  e.preventDefault();
  result.style.display = "none";
  loading.style.display = "block";

  setTimeout(() => {
    loading.style.display = "none";
    result.style.display = "block";
  }, 2000);
};

form.onsubmit = handleSubmit;
