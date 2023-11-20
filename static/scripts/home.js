function main() {
  let getStudentsButton = document.getElementById("getStudentsButton");
  let addCourseButton = document.getElementById("addCourseBtn");
  getStudentsButton.addEventListener("click", getStudents);
  addCourseButton.addEventListener("click", addCourse);
}

function getStudents() {
  fetch("/getRankedList", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((json) => populateTable(json));
}

function populateTable(json) {
  console.log(json);
  listElem = document.getElementById("studentOrderedList");
  listElem.innerHTML = "";
  for (let i = 0; i < json.length; i++) {
    if (json[i]["courses"].length == 0) {
      continue;
    }
    let li = document.createElement("li");
    let innerDiv = document.createElement("div");
    // Div will have the student name, an info button which on hover will display the student's email, and the courses they are taking

    // Student name
    let topRowDiv = document.createElement("div");
    topRowDiv.classList.add("topRowDiv");
    let name = document.createElement("p");
    name.innerHTML = json[i]["name"];
    topRowDiv.appendChild(name);

    // Info button
    let infoButton = document.createElement("button");
    infoButton.innerHTML = "i";
    infoButton.classList.add("infoButton");

    // Student email
    let email = document.createElement("p");
    email.innerHTML = json[i]["email"];
    email.classList.add("hidden");
    infoButton.addEventListener("mouseover", function() {
      email.classList.remove("hidden");
    });
    infoButton.addEventListener("mouseout", function() {
      email.classList.add("hidden");
    });
    topRowDiv.appendChild(email);
    topRowDiv.appendChild(infoButton);
    innerDiv.appendChild(topRowDiv);


    // Courses
    let coursesDiv = document.createElement("div");
    coursesDiv.classList.add("coursesDiv");
    let courses = json[i]["courses"];
    for (let j = 0; j < courses.length; j++) {
      let course = document.createElement("p");
      // Create string like: courses[j]["dept"] + " " + courses[j]["num"] + " " + courses[j]["section"]
      // With class "sameSection" if courses[j]["sameSection"] == true and class "diffSection" if courses[j]["sameSection"] == false
      let courseString = courses[j]["department"] + " " + courses[j]["courseCode"] + " " + courses[j]["sectionCode"];
      course.innerHTML = courseString;
      if (courses[j]["sameSection"] == true) {
        course.classList.add("sameSection");
      } else {
        course.classList.add("diffSection");
      }
      coursesDiv.appendChild(course);
      // !!!! TODO !!!!!! IMPLEMENT ACTUAL COURSE ELEMENTS
    }
    innerDiv.appendChild(coursesDiv);

    li.appendChild(innerDiv);
    listElem.appendChild(li);
  }
}

function addCourse() {
  // Create a new course element based on the info in the text boxes
  let courseDept = document.getElementById("deptCode").value;
  let courseNum = document.getElementById("courseCode").value;
  let courseSection = document.getElementById("sectionCode").value;
  let deleteCourseButton = document.createElement("button");
  deleteCourseButton.innerHTML = "X";
  deleteCourseButton.addEventListener("click", removeCourse);

  let table = document.getElementById("courseTable");
  // Unhide table
  table.classList.remove("hidden");

  // Add the new course
  let newRow = table.insertRow(-1);
  let deptCell = newRow.insertCell(0);
  let numCell = newRow.insertCell(1);
  let sectionCell = newRow.insertCell(2);
  let removeCell = newRow.insertCell(3);
  deptCell.innerHTML = courseDept;
  numCell.innerHTML = courseNum;
  sectionCell.innerHTML = courseSection;
  removeCell.appendChild(deleteCourseButton);


}

function removeCourse() {
  // Clear the current row
  currentRow = this.parentNode.parentNode;
  currentRow.innerHTML = "";

}

document.addEventListener('DOMContentLoaded', function() {
  main();
});