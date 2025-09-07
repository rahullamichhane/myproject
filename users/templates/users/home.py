<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        
    }
    
    .row {
        background-color:rgba(255, 99, 71, 0.5);
        padding: 120px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: center;
        radius:20px;
        
    }
    
    h3 {
        margin-bottom: 20px;
        color:Tomato;   
    }
    

    button {
        background-color: none;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 3px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    
    button:hover {
        background-color: Tomato;
    }
    
  
    
    a {
        color: green;
        text-decoration: none;
    }
</style>

<div class="container">
    <div class="row">
        {% if user.is_authenticated %}
            <div class="alert alert-success" role="alert">
            <h3>Welcome {{ user.username }}!</h3>
            <a href="{% url 'logout' %}">Logout?</a>
            </div>
        {% else %}
            <div class="alert alert-success" role="alert">
            <h3>Welcome!</h3>
            <button type="button">
            <a href="{% url 'register' %}">Signup</a>
            </button><br><br>
            <button class="button">
            <a href="{% url 'login' %}">Login</a>
            </button>
        </div>
        {% endif %}
    </div>
</div>