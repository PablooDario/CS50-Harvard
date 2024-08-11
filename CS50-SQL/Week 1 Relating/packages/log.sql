
-- *** The Lost Letter ***

-- Select the id's of the packages sent from 900 Somerville Avenue
SELECT id, to_address_id FROM packages WHERE from_address_id =(
    SELECT id FROM addresses WHERE address = '900 Somerville Avenue'
);

-- Find the correct address where the package should have arrived
SELECT * FROM addresses WHERE address LIKE '2 Finn%';

-- Select the id of the packages that have the destiny of 2 Finnigan Street
SELECT id FROM packages WHERE to_address_id =(
    SELECT id FROM addresses WHERE address LIKE '2 Finn%'
);

-- Select the id of the missing package
SELECT id FROM packages WHERE from_address_id =(
    SELECT id FROM addresses WHERE address = '900 Somerville Avenue'
) AND to_address_id =(
    SELECT id FROM addresses WHERE address LIKE '2 Finn%'
);

-- Select the address where the package was dropped off
SELECT address, type FROM addresses WHERE id = (
    SELECT address_id FROM scans WHERE action = 'Drop' AND package_id = (
        SELECT id FROM packages WHERE from_address_id = (
            SELECT id FROM addresses WHERE address = '900 Somerville Avenue'
        ) AND to_address_id = (
            SELECT id FROM addresses WHERE address LIKE '2 Finn%'
        )
    )
);

-- *** The Devious Delivery ***

--Check the packages that does not have from adress
SELECT * FROM packages WHERE from_address_id IS NULL;

-- Check the status of the package
SELECT * FROM scans WHERE package_id = (
    SELECT id FROM packages
    WHERE from_address_id IS NULL
);

-- Get the addres the package end up
SELECT * FROM addresses WHERE id = (
    SELECT address_id FROM scans WHERE package_id = (
        SELECT id FROM packages
        WHERE from_address_id IS NULL
    ) AND "action" = 'Drop'
);

-- *** The Forgotten Gift ***

-- Check if the from address is right
SELECT * FROM addresses WHERE address = '109 Tileston Street';

--Check the packages sent from this address
SELECT * FROM packages WHERE from_address_id = (
    SELECT id FROM addresses
    WHERE address = '109 Tileston Street'
);

-- Since it is a package, we will assume that this is the correct one and check the status of this package
SELECT * FROM scans WHERE package_id = (
    SELECT id FROM packages WHERE from_address_id = (
        SELECT id FROM addresses
        WHERE address = '109 Tileston Street'
    )
);

-- Get the name of the last driver who picked the package
SELECT * FROM drivers WHERE id =(
    SELECT driver_id FROM scans WHERE package_id = (
        SELECT id FROM packages WHERE from_address_id = (
            SELECT id FROM addresses
            WHERE address = '109 Tileston Street'
        )
    )
    ORDER BY timestamp DESC LIMIT 1
);