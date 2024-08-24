
--Create Table to store the encoded phrases
CREATE TABLE IF NOT EXISTS "phrases_encoded"(
    "id" INTEGER,
    "id_sentence" INTEGER,
    "begin_at" INTEGER,
    "length" INTEGER,
    PRIMARY KEY ("id")
);

--Create a Table to store the decoded phrases
CREATE TABLE IF NOT EXISTS "phrases_decoded"(
    "id" INTEGER,
    "phrase" TEXT,
    PRIMARY KEY ("id")
);

-- Create a Trigger to insert the decoded phrase when a new encoded phrase is inserted
CREATE TRIGGER "decode_phrases"
AFTER INSERT ON "phrases_encoded"
FOR EACH ROW
BEGIN
    INSERT INTO "phrases_decoded" ("id", "phrase")
    SELECT NEW."id",
           SUBSTR("sentence", NEW."begin_at", NEW."length")
    FROM "sentences"
    WHERE id = NEW."id_sentence";
END;

-- Insert encoded phrases
INSERT INTO "phrases_encoded" (id_sentence, begin_at, length)
VALUES (14, 98, 4),
(114, 3, 5),
(618, 72, 9),
(630, 7, 3),
(932, 12, 5),
(2230, 50, 7),
(2346, 44, 10),
(3041, 14, 5);

-- Craete view with the full message 
CREATE VIEW "message" AS
SELECT "phrase" FROM phrases_decoded;
