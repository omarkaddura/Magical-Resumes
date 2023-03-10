import bcrypt from "bcryptjs";
import User from "../../../models/User";
import dbConnect from "../../../utils/mongo";

export default async function register(req, res) {
  await dbConnect(); // connect database
  //Accepting only POST method
  if (req.method === "POST") {
    try {
      const { fullName, email, password } = req.body; // getting data from client through the request body
      // checking if input is valid
      if (!fullName || !email || !password) {
        return res.status(400).json({ message: "Please add all fields" });
      }
      //check if user already exists
      const userExists = await User.findOne({ email });
      if (userExists) {
        return res.status(400).json({ message: "User already exists" });
      }
      // salt for hashing size
      // hash for encrypting password
      const salt = bcrypt.genSaltSync(10);
      const hash = bcrypt.hashSync(password, salt);
      //creating user model
      const newUser = new User({
        fullName,
        email,
        password: hash,
      });
      // save usermodel to database
      await newUser.save();
      res.status(200).send("User has been created.");
    } catch (err) {
      console.log("lllllll", err);
      res.status(405).json({ err: err, message: "something is wrong" });
    }
  } else {
    res.status(405).json({ message: "We only support POST" });
  }
}