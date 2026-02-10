// Get references to DOM elements
const input = document.getElementById('todoInput');
const addBtn = document.getElementById('addBtn');
const todoList = document.getElementById('todoList');

// Function to add a new task
function addTask() {
    // Get task value text from user
    const taskValue = input.value.trim();
    
    // Prevent adding empty tasks
    if (taskValue === "") return;

    // Create the new list item
    const li = document.createElement('li');
    li.className = 'todo-item';

    // Create the checkbox
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', function() {
        li.classList.toggle('completed');
    });

    // Create the task text span
    const span = document.createElement('span');
    span.className = 'todo-text';
    span.textContent = taskValue;

    // Create the delete button
    const delBtn = document.createElement('button');
    delBtn.className = 'delete-btn';
    delBtn.textContent = '🗑';
    delBtn.onclick = function() {
        todoList.removeChild(li); // Remove the task from the list
    };

    // Append the elements to the list item
    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(delBtn);

    // Append the list item to the todo list
    todoList.appendChild(li);

    // Clear the input field
    input.value = "";
}

// To delete the list from To-Do-List
addBtn.addEventListener('click', addTask);

// "Enter" key is creates new list
input.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') addTask();
});
