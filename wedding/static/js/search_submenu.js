    let age_btn = document.getElementById('drop-down-age');
    age_btn.addEventListener('mouseover', function(e){
        document.getElementById('age-link').classList.add('show');
        document.getElementById('age-link').addEventListener('mouseover', function(e){
            document.getElementById('age-link').classList.add('show');
        });
    });
    age_btn.addEventListener('mouseleave', function(e){
        document.getElementById('age-link').classList.remove('show');
        document.getElementById('age-link').addEventListener('mouseleave', function(e){
            document.getElementById('age-link').classList.remove('show');
        });
    });

    let prof_btn = document.getElementById('drop-down-prof');
    prof_btn.addEventListener('mouseover', function(e){
        document.getElementById('prof-link').classList.add('show');
        document.getElementById('prof-link').addEventListener('mouseover', function(e){
            document.getElementById('prof-link').classList.add('show');
        });
    });
    prof_btn.addEventListener('mouseleave', function(e){
        document.getElementById('prof-link').classList.remove('show');
        document.getElementById('prof-link').addEventListener('mouseleave', function(e){
            document.getElementById('prof-link').classList.remove('show');
        });
    });

    let city_btn = document.getElementById('drop-down-city');
    city_btn.addEventListener('mouseover', function(e){
        document.getElementById('city-link').classList.add('show');
        document.getElementById('city-link').addEventListener('mouseover', function(e){
            document.getElementById('city-link').classList.add('show');
        });
    });
    city_btn.addEventListener('mouseleave', function(e){
        document.getElementById('city-link').classList.remove('show');
        document.getElementById('city-link').addEventListener('mouseleave', function(e){
            document.getElementById('city-link').classList.remove('show');
        });
    });
   
    // age check filtering
    let agelabel = document.querySelectorAll('#ages-label');
    let ageCheck = document.querySelectorAll('.ages');
    for(let i = 0; i < ageCheck.length; i++)
    {
        if(ageCheck[i+1]){
            for(let j = i; j < ageCheck.length; j++){
                if(ageCheck[j+1]){
                    if(ageCheck[i].value === ageCheck[j+1].value)
                    {
                        agelabel[j+1].remove();
                    }
                }
            }
        }
    }
    // profession filtering
    let proflabel = document.querySelectorAll('#prof-label');
    let profCheck = document.querySelectorAll('.prof');
    for(let i = 0; i < profCheck.length; i++)
    {
        if(profCheck[i+1]){
            for(let j = i; j < profCheck.length; j++){
                if(profCheck[j+1]){
                if(profCheck[i].value === profCheck[j+1].value)
                {
                    proflabel[j+1].remove();
                }
            }
            }
        }
    }

    //profession city filtering
    let citylabel = document.querySelectorAll('#city-label');
    let cityCheck = document.querySelectorAll('.city');
    for(let i = 0; i < cityCheck.length; i++)
    {
        if(cityCheck[i+1]){
            for(let j = i; j < cityCheck.length; j++){
                if(cityCheck[j+1]){
                    if(cityCheck[i].value === cityCheck[j+1].value)
                    {
                        citylabel[j+1].remove();
                    }
                }
            }
        }
    }