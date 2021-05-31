pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract CarRegistry is ERC721Full {
    constructor() public ERC721Full("CarRegistryToken", "CAR") {}

    struct carsInfo {
        address owner;
        string makeAndModel;
        uint256 expectedAppraisalValue;
    }

    mapping(uint256 => carsInfo) public carCollection;

    event Appraisal(uint256 tokenId, uint256 expectedValue, string reportURI);

    function registerCar(
        address owner,
        string memory makeAndModel,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        carCollection[tokenId] = carsInfo(owner, makeAndModel, initialAppraisalValue);

        return tokenId;
    }

    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {
        carCollection[tokenId].expectedAppraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        return carCollection[tokenId].expectedAppraisalValue;
    }
}
