class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
    let lowestPrice = Infinity;
    let maxProfit = 0;

        for (p of prices) {
        if (p < lowestPrice) lowestPrice = p;
        maxProfit = Math.max(maxProfit, p-lowestPrice);
    }

    return maxProfit;z
    }
}
