export const getSecondHalfOfTranscript = (transcript) => {
  const splitIndex = transcript[0].indexOf("], [");
  if (splitIndex === -1) {
    return "";
  }
  return transcript[0].substring(splitIndex + 3).trim();
};

export const extractTranscript = (jsonObj) => {
  let transcript = "";

  const extractText = (obj) => {
    if (typeof obj === "string") {
      transcript += obj + " ";
    } else if (Array.isArray(obj)) {
      obj.forEach(extractText);
    } else if (typeof obj === "object" && obj !== null) {
      Object.values(obj).forEach(extractText);
    }
  };

  extractText(jsonObj);
  return transcript.trim();
};
