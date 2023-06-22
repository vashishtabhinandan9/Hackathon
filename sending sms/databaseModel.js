const mongoose = require("mongoose");

const CrimeSchema = new mongoose.Schema(
  {
    alertLevel: {
      type: String,
      required:true,
      lowercase:true,

    },
    crime: {
      type: String, 
      required : [true,"please provide type of crime"] ,
      lowercase:true,
     
    },
    location: {
        type: String, 
        required : true ,
        lowercase:true,
     
      },
    Pic: {
        type: Array,
        required: false,
      },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Crime", CrimeSchema);