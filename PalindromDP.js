ascii_a = "a".charCodeAt();
ascii_z = "z".charCodeAt();
ascii_A = "A".charCodeAt();
ascii_Z = "Z".charCodeAt();
ascii_0 = "0".charCodeAt();
ascii_9 = "9".charCodeAt();

function isValid(char){
    // function that enters a character and verifies that it is a letter or a number
    var ascii_char = char.charCodeAt();
    if((ascii_char >= ascii_a && ascii_char <= ascii_z) 
    || (ascii_char >= ascii_A && ascii_char <= ascii_Z) 
    || (ascii_char >= ascii_0 && ascii_char <= ascii_9)){
        return true;
    }
    return false;
};

function LongestPalindromicSubstring(phraseOriginal){
    // function that enters a string and retorn a sorted list of all palindromic subsequences
    var phrase = new Array();
	var index = new Array(); 
	var i = 0;
	while(i<phraseOriginal.length){ //generate a reduces string with only the letters
	    while(i<phraseOriginal.length && !isValid(phraseOriginal[i])) i++
	    phrase.push(phraseOriginal[i]);
	    index.push(i);
	    i++;
	}
	
	var len = phrase.length;
	var ans = []; 
	var table = new Array(len); 
	for (i = 0; i < len; i++){ // Base case, all subsequences of long 1 are palindrom
    	table[i] = new Array(len);
    	table[i][i] = true; 
    }
    for (l = 2; l <= len; l++) { // inductive case
        for (i = 0; i < len - l + 1; i++) {
            var j = i + l - 1;
            if (table[i + 1][j - 1] && phrase[i].toLowerCase() == phrase[j].toLowerCase()) { 
                table[i][j] = true; 
                ans.push(phraseOriginal.substring(index[i],index[j]+1))
            }
        } 
    }
    return ans;
};
console.log(LongestPalindromicSubstring("Llego a la tierra y le dijo: Dabale arroz a la zorra el abad, ella acepto oso"));