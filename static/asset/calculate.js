import { getCookie } from "./util.js";

const form = document.getElementById("form");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const weight_of_sample = document.getElementById("weight_of_sample").value;
const weight_of_empty_flask = document.getElementById(
  "weight_of_empty_flask"
).value;
const weight_of_flask = document.getElementById("weight_of_flask").value;
const weight_of_oil = document.getElementById("weight_of_oil").value;
const csrfToken = getCookie("csrftoken");

const handleSubmit = async (e) => {
  try {
    e?.preventDefault && e.preventDefault();
    result.style.display = "none";
    loading.style.display = "block";

    console.log({
      weight_of_sample,
      weight_of_empty_flask,
      weight_of_flask,
      weight_of_oil,
      csrfToken,
    });

    const response = await fetch(
      "http://127.0.0.1:8000/calculate_percentage_of_fat/",
      {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken, // Include CSRF token
          Origin: "http://127.0.0.1:8000",
        },
        body: {
          weight_of_flask,
          weight_of_oil,
          weight_of_empty_flask,
          weight_of_sample,
        },
      }
    );

    const jsonResponse = await response.json();

    result.innerHTML = jsonResponse.response_message || jsonResponse.error;

    loading.style.display = "none";
    result.style.display = "block";
  } catch (err) {
    console.log(err);
  }
};

form.onsubmit = handleSubmit;
