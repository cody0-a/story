import {Navigate} from "react-router-dom"
import jwtDecode from 'jwt-decode'
import api from "../api"
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"
import { useState,useEffect } from "react"


function ProtectedRoute({children}) {

    const [isAuthorized, setIsAuthorized] = useState(false) 

    useEffect(()=>{
        auth().catch() 
        setIsAuthorized(true)
        
    } ,[])

    const refreshToken =  async () =>{

        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try{

            const response = await api.post('/api/token/refresh', {
                refresh : refreshToken    

        });
        if(response.status === 200){

            localStorage.setItem(ACCESS_TOKEN, response.data.access)
            setIsAuthorized(true)
        }
        else{
            setIsAuthorized(false)
        }
        

        }

        catch(error){
            setIsAuthorized(false)
            console.log(error)

        }

    }

    


    const auth = async () =>{
        const token = localStorage.getItem(ACCESS_TOKEN)
        if(! token){
            setIsAuthorized(false)
            return
        }
        const decoded = jwtDecode(token)
        const tokenExpiration  = decoded.exp
        const now = Date.now()/1000
        if (tokenExpiration < now){
            await refreshToken()
        }
        else{
            setIsAuthorized(true)
        }

    }

    if (isAuthorized){
        <div> loading...</div>
    }

    else{
        return isAuthorized ===true ? children : <Navigate to='login'/>
    }
}



  export default ProtectedRoute;