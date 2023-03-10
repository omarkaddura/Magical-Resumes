import React, { useState } from 'react'
import classes from "../styles/Home.module.css"
function register() {

   const [formData,setFormData]=useState({ fullName: "",
          email: "",
          password: "",})


const handleChange =(e)=>{
    
    setFormData(p=>{
     return {  ...p,
        [e.target.name]:e.target.value}
    })

}
const handleSubmit =(e)=>{
    e.preventDefault()
const request = fetch("http://localhost:3000/api/auth/register",{
 method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(formData),
})

}
  return (
    <div  className={classes.container}>
        <form
        className={classes.container}
        onSubmit={handleSubmit}>

 <input

              placeholder="Enter Full Name"
            //   label={"Full name"}
              type="text"
              id="fullName"
              name="fullName"
              value={formData.fullName}
              onChange={handleChange}
              />
<input
            //   label={"email"}
              type="email"
              id="email"
              name="email"
              placeholder="Enter your personal e-mail"
              value={formData.email}
              onChange={handleChange}
              />
                    <input
              name="password"
              type="password"
              id="password"
              placeholder="Enter Password"
            //   label={"Password"}
              onChange={handleChange}
              value={formData.password}
              />
              <button type="submit" >
              Submit
            </button>
              </form>
    </div>
  )
}

export default register