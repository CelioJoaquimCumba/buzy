document.addEventListener('DOMContentLoaded',()=>{

    //Login form
    let login_form = document.querySelector('#login_form');
    if ( login_form ) {

        login_form.onsubmit = ()=>{

            let username = document.querySelector('#username').value;
            let password = document.querySelector('#password').value;

            if ( username.trim() == "" ) {
                let error_username = document.querySelector('#error_username')
                error_username.style.display = 'block';
                setTimeout( ()=>error_username.style.display = 'none',2000)
                return false;
            }
            if ( password.trim() == "" ) {
                let error_password = document.querySelector('#error_password')
                error_password.style.display = 'block';
                setTimeout( ()=>error_password.style.display = 'none', 2000)
                return false;
            }
            return true;
           
        }

        let username = document.querySelector('#username')

    }

    //logout form
    logout_form = document.querySelector('#logout_form');
    if ( logout_form ) {

        logout_form.onsubmit = ()=>{

            let username = document.querySelector('#username').value;
            let password = document.querySelector('#password').value;
            let email = document.querySelector('#email').value

            if ( username.trim() == "" ) {
                let error_username = document.querySelector('#error_username')
                error_username.style.display = 'block';
                setTimeout( ()=>error_username.style.display = 'none',2000)
                return false;
            }
            if ( email.trim() == "" ) {
                let error_email = document.querySelector('#error_email')
                error_email.style.display = 'block';
                setTimeout( ()=>error_email.style.display = 'none', 2000)
                return false;
            }
            if ( password.trim() == "" ) {
                let error_password = document.querySelector('#error_password')
                error_password.style.display = 'block';
                setTimeout( ()=>error_password.style.display = 'none', 2000)
                return false;
            }
            
            return true;

        }

    }

    //create form
    create_form = document.querySelector('#create_form');
    if ( create_form ) {



    }

    //following form
    following_form = document.querySelector('#following_form');
    if ( following_form ) {



    }

    //createActivity form
    createActivity = document.querySelector('#createActivity_form');
    if ( createActivity ) {
        let type_field = document.querySelector('#type')
        let div_product = document.querySelector('#div_product')
        let div_color = document.querySelector('#div_color')
        let div_name = document.querySelector('#div_name')
        let div_description = document.querySelector('#div_description')
        let div_participants = document.querySelector('#div_participants')
        let div_investement = document.querySelector('#div_investement')
        let div_gain = document.querySelector('#div_gain')
        let div_client = document.querySelector('#div_client')
        
        divs = [div_product,div_color,div_name,div_description,div_participants,div_investement,div_gain, div_client]

        
        // TODO Check to see empty fields

        //Switch field based on type
        let type = 'custom'
        type_field.onchange = ()=>{
            switch (type_field.value) {
                case 'deposit':
                    type='deposit'
                    break;
                case 'withdraw':
                    type ='withdraw';
                    
                    break;
                case 'purchase':
                    type = 'purchase'
                    break;
                case 'refund':
                    type = 'refund'
                    break;
                default:
                    type = 'custom'
                    break;
            }
            for ( let div in divs ){
                
                divs[div].style.display = 'none';
                divs[div].firstElementChild.required = "";
                if ( (type == 'deposit' || type == 'withdraw' || type == 'custom') && div == 4 ){
                    divs[div].style.display = 'block';
                    divs[div].firstElementChild.required = "required";
                    
                }
                if (type =='deposit' && div == 6 ) {
                    divs[div].style.display = 'block';
                    divs[div].firstElementChild.placeholder = 'Deposit amount'
                    divs[div].firstElementChild.required = "required";
                }
                if (type =='withdraw' && div == 5) {
                    divs[div].style.display = 'block';
                    divs[div].firstElementChild.placeholder = 'Withdraw amount'
                    divs[div].firstElementChild.required = "required";
                }
                if ( (type == 'purchase' || type == 'refund') && (div == 0 || (div == 1 && type == "purchase") || div == 4 || div == 7) ) {
                    divs[div].style.display = 'block';
                    divs[div].firstElementChild.required = "required";
                }
                if ( type=='custom' && (div != 0 && div != 1 && div !=7 ) ){
                    divs[div].style.display = 'block';
                    divs[div].firstElementChild.required = "required";
                }
            }

        };
        
        




    }


});




