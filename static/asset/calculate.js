import { getCookie } from "./util.js";

const form = document.getElementById("form");
const loading = document.getElementById("loading");
const result = document.getElementById("result");

const handleSubmit = async (e) => {
  try {
    e?.preventDefault && e.preventDefault();
    result.style.display = "none";
    loading.style.display = "block";

    const weight_of_sample = document.getElementById("weight_of_sample").value;
    const weight_of_empty_flask = document.getElementById("weight_of_empty_flask").value;
    const weight_of_flask = document.getElementById("weight_of_flask").value;
    const weight_of_oil = document.getElementById("weight_of_oil").value;
    const csrfToken = getCookie("csrftoken");

    console.log("Weight of Sample:", weight_of_sample);
    console.log("Weight of Empty Flask:", weight_of_empty_flask);
    console.log("Weight of Flask:", weight_of_flask);
    console.log("Weight of Oil:", weight_of_oil);
    
    const bodyData = {
      weight_of_flask,
      weight_of_oil,
      weight_of_empty_flask,
      weight_of_sample,
    };

    console.log("Form Data:", bodyData);

    const response = await fetch("http://127.0.0.1:8000/calculate_percentage_of_fat/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
        "Origin": "http://127.0.0.1:8000",
      },
      body: JSON.stringify(bodyData),
    });

    const jsonResponse = await response.json();

    result.innerHTML = jsonResponse.response_message || jsonResponse.error;

    loading.style.display = "none";
    result.style.display = "block";
  } catch (err) {
    console.error(err);
  }
};

form.onsubmit = handleSubmit;
