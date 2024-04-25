import { getCookie } from "./util.js";

const form = document.getElementById("form");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const fvw = document.getElementById("fvw").value || "0";
const cm = document.getElementById("cm").value || "0";
const mc = document.getElementById("mc").value || "0";
const vsc = document.getElementById("vsc").value || "0";
const csrfToken = getCookie("csrftoken");

const handleSubmit = async (e) => {
  try {
    e?.preventDefault && e.preventDefault();
    result.style.display = "none";
    loading.style.display = "block";

    console.log({ fvw, cm, mc, vsc, csrfToken });

    const response = await fetch(
      "http://127.0.0.1:8000/calculate_percentage_of_fat/",
      {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken, // Include CSRF token
          Origin: "http://127.0.0.1:8000",
        },
        body: {
          weight_of_flask: fvw,
          weight_of_oil: cm,
          weight_of_empty_flask: mc,
          weight_of_sample: vsc,
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
