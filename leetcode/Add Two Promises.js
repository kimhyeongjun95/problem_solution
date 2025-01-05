/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function (promise1, promise2) {
  return await Promise.all([promise1, promise2]).then(([v1, v2]) => v1 + v2);
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */

promise1 = new Promise((resolve) => setTimeout(() => resolve(2), 20));
promise2 = new Promise((resolve) => setTimeout(() => resolve(5), 60));
console.log(addTwoPromises(promise1, promise2)); // 7;

promise3 = new Promise((resolve) => setTimeout(() => resolve(2), 20));
promise4 = new Promise((resolve) => setTimeout(() => resolve(5), 60));
console.log(addTwoPromises(promise3, promise4)); // -2;
