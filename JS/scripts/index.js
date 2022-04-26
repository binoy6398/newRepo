window.onload = async() => {
    const timeField = document.getElementById("time")
    injectTime(timeField)
   preFetchBgImages()
   getImagesFromLocalStorage()
}
 

const preFetchBgImages = async() => {
    const bgImages = await Promise.all(Array(10).fill(1).map((x) => getRandomBgImage()))
    window.localStorage.setItem("bgImageUrl",JSON.stringify(bgImages))
}

const getBgImageLocalStorage = () => {
    const images = window.localStorage.getItem("bgImageUrl")
    if(images)
    {
        try {
            const ImagesArray = JSON.parse(images)
            if(ImagesArray.length > 0)
            return ImagesArray[0]
        } catch (error) {
            console.log("Error while paring bgImage array from local storage")
        }
    }
}



const injectTime = (field) => {
    setInterval(()=>{
    field.innerText = new Date().toTimeString().split(" ")[0]
    },[500])
}


const tags = ["space","natural","landscape"]




const getRandomTag = (tags) => {
    if (tags.length === 0 ) throw new Error("Tag array is empty")
    const randomNumber = Math.floor(Math.random() * tags.length)
    return tags[randomNumber]
}

const generateUrl = () =>{
    const tag = getRandomTag(tags)
    return `https://source.unsplash.com/1600x900/?${tag}`
}


const getRandomBgImage = async () => {
    const url = generateUrl()
    const response = await fetch(url,{method:"GET"})
    if(response.status === 200){
       return response.url
    }else{
        throw new Error("Error while fetching image from unsplash")
    }
}


const changeBg = async () => {
    const newImage = await getRandomBgImage()
    document.body.style.backgroundImage = `url(${newImage})`
}




