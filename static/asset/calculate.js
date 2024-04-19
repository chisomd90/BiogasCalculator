import { getCookie } from "./util.js";

const form = document.getElementById("form");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const fvw = parseFloat(document.getElementById("fvw").value || 0);
const cm = parseFloat(document.getElementById("cm").value || 0);
const mc = parseFloat(document.getElementById("mc").value || 0);
const vsc = parseFloat(document.getElementById("vsc").value || 0);
const csrfToken = getCookie("csrftoken");

const handleSubmit = async (e) => {
  try {
    e?.preventDefault && e.preventDefault();
    result.style.display = "none";
    loading.style.display = "block";

    console.log({ fvw, cm, mc, vsc });

    const response = await fetch("http://127.0.0.1:8000/calculate-biogas/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken, // Include CSRF token
        Origin: "http://127.0.0.1:8000",
      },
      body: {
        ratio_fvw: fvw,
        ratio_cow_manure: cm,
        moisture_content: mc,
        vs_content: vsc,
      },
    });

    console.log(response);

    setTimeout(() => {
      loading.style.display = "none";
      result.style.display = "block";
    }, 2000);
  } catch (err) {
    console.log(err);
  }
};

form.onsubmit = handleSubmit;