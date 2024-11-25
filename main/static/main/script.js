function toggleForm() {
    const mainActionBtn = document.getElementById('main-action-btn');
    const toggleBtn = document.getElementById('toggle-btn');
    const formTitle = document.getElementById('form-title');
    const doctorFields = document.getElementById('doctor-fields');
    const patientFields = document.getElementById('patient-fields');
    const userForm = document.getElementById('user-form');

    if (mainActionBtn.innerText === 'Увійти') {
        mainActionBtn.innerText = 'Зареєструватися';
        toggleBtn.innerText = 'Повернутися до входу';
        formTitle.innerText = 'Реєстрація';
        userForm.action = "/users/register/";
        toggleUserFields();
    } else {
        mainActionBtn.innerText = 'Увійти';
        toggleBtn.innerText = 'Зареєструватися';
        formTitle.innerText = 'Вхід';
        userForm.action = "/users/login/";
        doctorFields.style.display = 'none';
        patientFields.style.display = 'none';
    }
}
function toggleUserFields() {
    const doctorFields = document.getElementById('doctor-fields');
    const patientFields = document.getElementById('patient-fields');
    const userType = document.querySelector('input[name="user_type"]:checked').value;

    if (document.getElementById('main-action-btn').innerText === 'Зареєструватися') {
        if (userType === 'doctor') {
            doctorFields.style.display = 'block';
            patientFields.style.display = 'none';
        } else if (userType === 'patient') {
            doctorFields.style.display = 'none';
            patientFields.style.display = 'block';
        }
    } else {
        doctorFields.style.display = 'none';
        patientFields.style.display = 'none';
    }
}
