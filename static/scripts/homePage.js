function main() {
  let button = document.getElementById("getStudentsButton");
  button.addEventListener("click", getStudents);
}

function getStudents() {
  fetch("/getRankedList", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
}

document.addEventListener('DOMContentLoaded', function() {
  main();
});