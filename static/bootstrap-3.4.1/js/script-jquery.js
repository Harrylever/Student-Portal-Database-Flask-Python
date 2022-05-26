window.onload = function () {

    let phone_number_boolean;
    let jambscore_boolean;

    $('#portal_student_form').submit(function () {
        let firstname = $('#firstname').val();
        let lastname = $('#lastname').val();
        let dateofbirth = $('#dateofbirth').val();
        let phonenumber = $('#phonenumber').val();
        let gender = document.querySelector('input[name="gender"]:checked').value;
        let state = $('#state').val();
        let nextofkin = $('#nextofkin').val();
        let middlename = $('#middlename').val();
        let emailaddress = $('#emailaddress').val();
        let address = $('#address').val();
        let local = $('#local').val();
        let jambscore = $('#jambscore').val();
        let admis_status = "undecided";

        if ((phonenumber.length < 11) || (phonenumber.length > 11)) {
            document.getElementById("phonenumberError").innerHTML = "Phone number must be 11 digits";
            phone_number_boolean = false;
        } else {
            document.getElementById("phonenumberError").innerHTML = "";
            phone_number_boolean = true;
        }

        if ((jambscore.length < 3) || (jambscore.length > 3)) {
            document.getElementById("jambscoreError").innerHTML = "Jamb Score must be 3 digits";
            jambscore_boolean = false
        } else {
            document.getElementById("jambscoreError").innerHTML = "";
            jambscore_boolean = true;
        }

        if ((phone_number_boolean == true) && (jambscore_boolean == true)) {
            $.ajax({
                type: "POST",
                url: "/student",
                data: JSON.stringify({
                    'firstname': firstname,
                    'lastname': lastname,
                    'dateofbirth': dateofbirth,
                    'phonenumber': phonenumber,
                    'state': state,
                    "gender": gender,
                    'nextofkin': nextofkin,
                    'middlename': middlename,
                    'emailaddress': emailaddress,
                    'address': address,
                    'local': local,
                    'jambscore': jambscore,
                    'admis_status': admis_status
                }),
                dataType: "json",
                contentType: 'application/json, charset=UTF-8',
                success: function (data) {
                    location.assign("http://127.0.0.1:5051/admin/dashboard");
                    // location.reload();
                },
                error: function (err) {
                    console.log(err);
                }
            });
        }
    });


    $('#update_admis_status').submit(function() {

        let admis_status_selected = ''

        let admis_status = $('#admission_status_select').val();
        let student_id = document.getElementById('student_id').innerHTML;
        
        if (admis_status == "null" || admis_status == "undecided") {
            admis_status_selected = "undecided";
        }
        if (admis_status == "admitted") {
            admis_status_selected = "admitted"
        }
        // alert(student_id + " " + admis_status_selected)
        $.ajax({
            url: "/updateadmisstatus",
            type: "POST",
            data: JSON.stringify({
                'admis_status': admis_status_selected,
                'student_id': student_id,
            }),
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                location.reload();
            },
            error: function (err) {
                console.log(err)
            }
        });
    });


    $('#updateProfilPic').submit(function () {
        let data = new FormData();
        let student_id = document.getElementById('student_id').innerHTML;
        data.append('file', $('#profImage')[0].files[0]);
        data.append('student_id', student_id);
        // data.append('student_id', JSON.stringify({ 'student_id': student_id }));

        $.ajax({
            url: "/student/addprofileimg",
            type: "POST",
            data: data,
            // enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            success: function (data) {
                location.reload();
            },
            error: function (err) {
                console.log(err);
            }
        });
    });

}