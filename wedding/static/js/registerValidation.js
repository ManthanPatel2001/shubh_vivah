let next = document.getElementById('next');
let prev = document.getElementById('prev');
let submit = document.getElementById('submit');
let state = document.getElementById('state');
let today = new Date();
let dd = today.getDate();
let mm = today.getMonth() + 1;
let yyyy = today.getFullYear() - 21;
let year_min = today.getFullYear() - 70;

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
today = yyyy + '-' + mm + '-' + dd;
min = year_min + '-' + mm + '-' + dd;
document.getElementById("birth_date").setAttribute("max", today);
document.getElementById("birth_date").setAttribute("min", min);

function date_validate(){
    let date_value = document.getElementById("birth_date").value;
    if (date_value > today){
        document.getElementById('alertBox-look').classList.remove('d-none')
        document.getElementById('alertBox-look').innerHTML = 'Please Enter Valid Date'
    }else if(date_value < min){
        document.getElementById('alertBox-look').classList.remove('d-none')
        document.getElementById('alertBox-look').innerHTML = 'Please Enter Valid Date'
    }else{
        document.getElementById('alertBox-look').classList.add('d-none')
    }



}



const cityState = {
    'Gujarat':['Ahmedabad','Surat','Rajkot'],
    'Assam':['Guwahati', 'Silchar', 'Dibrugarh'],
    'Bihar':['Patna', 'Gaya', 'Bhagalpur']
}
state.addEventListener('change',function(){
    let city = document.getElementById('city');
    let state_val = state.value;
    city.options.length=0;
    for(let i = 0; i < cityState[state_val].length; i++ ){
        var opt = document.createElement('option');
        opt.value = cityState[state_val][i];
        opt.innerHTML = cityState[state_val][i];
        city.appendChild(opt);
    }
})

function mobile_check(){
    let mobile = document.getElementById('mobile').value;
    if(isNaN(mobile) === true){
        document.getElementById('alertBox-mobile').classList.remove('d-none')
        document.getElementById('alertBox-mobile').innerHTML = 'Please Enter valid Mobile Number'
    }
    else if(mobile.length != 10){
        document.getElementById('alertBox-mobile').classList.remove('d-none')
        document.getElementById('alertBox-mobile').innerHTML = 'Please Enter 10 digit Mobile Number'
    }else{
        document.getElementById('alertBox-mobile').classList.add('d-none');
    }
}

next.addEventListener('click', function(){
    let all_alert = document.getElementsByClassName('alert-warning')
    for(let i = 0; i < all_alert.length; i++){
        all_alert[i].classList.add('d-none');
    }


    let fname = document.getElementById('fname').value;
    let lname = document.getElementById('lname').value;
    let email_check = document.getElementById('user_email').value;
    let pass = document.getElementById('pass').value;
    let confPass = document.getElementById('confPass').value;
    let state = document.getElementById('state').value;
    let city = document.getElementById('city').value;
    let mobile = document.getElementById('mobile').value;
    
    const validRegex  = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(fname === '' || lname === ''){
        document.getElementById('alertBox-name').classList.remove('d-none')
        document.getElementById('alertBox-name').innerHTML = 'Please Enter Your Full Name'
    }else if(!email_check.match(validRegex) || isNaN(parseInt(email_check[0])) === false){
        document.getElementById('alertBox-email').classList.remove('d-none')
        document.getElementById('alertBox-email').innerHTML = 'Please Enter Valid Email ID'
    }else if(pass < 3){
        document.getElementById('alertBox-pass').classList.remove('d-none')
        document.getElementById('alertBox-pass').innerHTML = 'Please Enter Minimum 3 digit Password'
    }else if (pass !== confPass){
        document.getElementById('alertBox-pass').classList.remove('d-none')
        document.getElementById('alertBox-pass').innerHTML = 'Both Passwords does not Match'
    }else if(state === '' || city === ''){
        document.getElementById('alertBox-state').classList.remove('d-none')
        document.getElementById('alertBox-state').innerHTML = 'Please Enter State and City'
    }else if(mobile === ''){
        document.getElementById('alertBox-mobile').classList.remove('d-none')
        document.getElementById('alertBox-mobile').innerHTML = 'Please Enter valid Mobile Number'
    }else{
        document.getElementById("first-form").classList.toggle("visible");
        document.getElementById("sec-form").classList.toggle("visible");
    }

});


prev.addEventListener('click', function(){
    document.getElementById("first-form").classList.toggle("visible");
    document.getElementById("sec-form").classList.toggle("visible");
});

submit.addEventListener('click',function(e){
    let all_alert = document.getElementsByClassName('alert-warning');

    let look = document.getElementById('look').value;
    let birth_date = document.getElementById('birth_date').value;
    let mothertoung = document.getElementById('mothertoung').value;
    let prof = document.getElementById('prof').value;
    let qualify = document.getElementById('qualify').value;
    let religene = document.getElementById('religene').value;
    let cast = document.getElementById('cast').value;

    for(let i = 0; i < all_alert.length; i++){
        all_alert[i].classList.add('d-none');
    }

    if(look === ''){
        e.preventDefault();
        document.getElementById('alertBox-look').classList.remove('d-none')
        document.getElementById('alertBox-look').innerHTML = 'Please Enter Your Gender'
    }else if (birth_date == ''){
        e.preventDefault();
        document.getElementById('alertBox-look').classList.remove('d-none')
        document.getElementById('alertBox-look').innerHTML = 'Please Enter Your Birthdate'
    }else if(birth_date > today){
        e.preventDefault();
        document.getElementById('alertBox-look').classList.remove('d-none')
        document.getElementById('alertBox-look').innerHTML = 'Please Enter Valid Date'
    }else if(birth_date < min){
        e.preventDefault();
        document.getElementById('alertBox-look').classList.remove('d-none')
        document.getElementById('alertBox-look').innerHTML = 'Please Enter Valid Date'
    }else if(qualify == ''){
        e.preventDefault();
        document.getElementById('alertBox-qualify').classList.remove('d-none')
        document.getElementById('alertBox-qualify').innerHTML = 'Plese Enter Your Qualification'
    }else if(prof == ''){
        e.preventDefault();
        document.getElementById('alertBox-prof').classList.remove('d-none')
        document.getElementById('alertBox-prof').innerHTML = 'Please Enter Your Profession'
    }else if(mothertoung == ''){
        e.preventDefault();
        document.getElementById('alertBox-mothertoung').classList.remove('d-none')
        document.getElementById('alertBox-mothertoung').innerHTML = 'Please Enter Your MotherTounge'
    }else if(cast == ''){
        e.preventDefault();
        document.getElementById('alertBox-religene').classList.remove('d-none')
        document.getElementById('alertBox-religene').innerHTML = 'Please Enter Your Cast'
    }else if(religene == ''){
        e.preventDefault();
        document.getElementById('alertBox-religene').classList.remove('d-none')
        document.getElementById('alertBox-religene').innerHTML = 'Please Enter Your Religene'
    }
})

document.getElementById('showPass').addEventListener('click',function(){
    let pass = document.getElementById('pass')
    if (pass.getAttribute('type') === 'password'){
        pass.setAttribute('type','text');
    }else{
        pass.setAttribute('type','password');
    }
    });