export const getSecondHalfOfTranscript = (transcript) => {
  const splitIndex = transcript[0].indexOf("], [");
  if (splitIndex === -1) {
    return "";
  }
  return transcript[0].substring(splitIndex + 3).trim();
};
