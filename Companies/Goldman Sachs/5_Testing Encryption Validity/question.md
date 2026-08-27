**2. Testing Encryption Validity**

Encryption is the process of converting information algorithmically so that only a valid recipient can read the information before the end of its validity period.

For a each encrypted message, we are given:

* the instructionCount, i.e., the number of keys that a hijacker can test per second in order to try and crack the code
* validityPeriod
* a list of keys that can tested by the hijacker

Leveraging this information, our goal is to determine if the hijacker can crack the code within its validity period. Each test will need return two items:

1. If the hijacker cracks the code within its validity period (1 if true, 0 if false)
2. The strength of the encryption (cf. further below to read about the definition of strength)

The strength of the encryption **is the number of keys that must be tested to break the encryption**. It is defined as the product: d_max * 10^5, where d_max is the **maximum number of divisors** possible within the set of keys:

* keys is a list of positive integers, keys[i], that act as keys.
* the number of divisors (or divisibility) of an element is the number of elements in the set keys that are greater than 1 and are divisors of the element, i.e. element modulo divisor = 0.
* the element m that has the maximum number of divisors in keys determines d_max.

**Notes:**

* Any divisor of a key must be greater than 1.
* The list may contain duplicates - e.g., if keys = [2, 4, 4], the strength is 3 * 10^5, as 4 can be divided by 2 and 4 respectively, so 4 has 3 divisors in the list of keys.

**Example:**

* instructionCount = 1000
* validityPeriod = 10000
* keys = [2, 4, 8, 2]

Looking at the elements in keys, in order of appearance:

* 2 is divisible by [2, 2] so its degree of divisibility is 2
* 4 is divisible by [2, 4, 2] so its degree of divisibility is 3
* 8 is divisible by [2, 4, 8, 2] so its degree of divisibility is 4
* 2 is divisible by [2, 2] so its degree of divisibility is 2, as in the first case

The element m that has the maximum number of divisors is 8 and its degree of divisibility is 4. The encryption strength is 4 * 10^5 = 400,000.

In this example, the hijacker can test 1000 keys per second (instructionCount) and the encrypted message has a validity period of 10 000 seconds (validityPeriod), which means that the hijacker can test 1000 * 10000 = 10^7 keys while the message is still valid. This is greater than the encryption strength, so the hijacker can expect to crack the code.

The expected array is hence [1, 400000] because the hijacker can decrypt the message in time, and the strength of the encryption is 400000.

**Function Description**

Complete the function encryptionValidity in the editor below.

encryptionValidity has the following parameters:

* int instructionCount: an integer, the number of keys the hijacker can test per second
* int validityPeriod: an integer, the number of seconds the message must be protected
* int keys[n]: an array of integers, keys for encryption/decryption

**Returns:**

* List [int, int]: 2 element integer array result containing the expected outputs described above.

**Constraints**

* 1 <= instructionCount, validityPeriod <= 10^8
* 1 <= n <= 10^5